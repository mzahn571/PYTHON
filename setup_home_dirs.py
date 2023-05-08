#!/apollo/env/PirateOwlOpsTools/bin/python3

# Import common functions
from common_functions import *

def symlink_file(path, owner='root', group='root'):
    '''
    Symlink file, if file exists at destination it is removed and replaced

    Parameter:
    path: A path-like object representing a file system path
    type: str

    owner: user that should own directory, defaults to root
    type: str

    group: group that should own directory, defaults to root

    Return: None
    '''
    uid = pwd.getpwnam(owner).pw_uid
    gid = grp.getgrnam(group)[2]

    # Full path of files to symlink from Apollo environment
    source_path = f'{os.path.dirname(os.path.abspath(__file__))}/configuration/directories/{path}'

    # Get the list of all files in directory tree from source_path
    list_of_files = list()
    for (dirpath, dirnames, filenames) in os.walk(source_path):
        list_of_files += [os.path.join(dirpath, file) for file in filenames]

    # Loop to create symlinks
    for elem in list_of_files:
        path_list=elem.split(f'{path}/')
        source_file = path_list[-1]
        destination_file = f'{path}/{source_file}'

        # Remove destination file if it exists
        if os.path.exists(destination_file):
            os.remove(destination_file)
        
        # Create Symlink to destination_file
        destination_directory = os.path.dirname(destination_file)
        if not os.path.isdir(destination_directory):
            Path(destination_directory).mkdir(parents=True, exist_ok=True)
            os.chown(destination_directory, uid, gid)
        os.symlink(elem, destination_file)
        os.chown(destination_file, uid, gid)

def append_bashrc_variables(string_to_append):
    '''
    Append variables to /etc/bashrc (System default bashrc for all accounts)

    Parameter:
    string_to_append: Value to look for in file and append if missing
    type: str

    Return: None
    '''
    bash_rc = open('/etc/bashrc', 'r')

    # Check if string to add already exists
    if string_to_append in bash_rc.read():
        print(f'{string_to_append} set in /etc/bashrc, skipping')
    else:
        bash_rc.close()
        bash_rc = open('/etc/bashrc', 'a+')
        print(f'Setting {string_to_append} in /etc/bashrc')
        bash_rc.write(f'#Set by Ops Tools\n{string_to_append}\n')
    bash_rc.close()

def append_zshrc_variables(string_to_append):
    '''
    Append variables to /etc/zshrc (System default zshrc for all accounts)

    Parameter:
    string_to_append: Value to look for in file and append if missing
    type: str

    Return: None
    '''
    zsh_rc = open('/etc/zshrc', 'r')

    # Check if string to add already exists
    if string_to_append in zsh_rc.read():
        print(f'{string_to_append} set in /etc/zshrc, skipping')
    else:
        zsh_rc.close()
        zsh_rc = open('/etc/zshrc', 'a+')
        print(f'Setting {string_to_append} in /etc/zshrc')
        zsh_rc.write(f'#Set by Ops Tools\n{string_to_append}\n')
    zsh_rc.close()

def main():
    # Group ID for "pirate-owls" POSIX group, this differs across partitions (AWS, AWS-Gov, AWS-ISO, AWS-ISOB, etc)
    posix_group_id = grp.getgrnam('pirate-owls')[2]
    
    # Get list of users currently in POSIX group so we can validate they exist on the host
    user_list = get_users_from_gid(posix_group_id)
    
    # Append ${REGION}, ${PARTITION}, and ${AIRPORT} variables to /etc/bashrc and /etc/zshrc
    airport = get_my_airport_code()
    region = get_my_region(airport)
    partition = get_my_partition(airport)
    append_bashrc_variables(f'AIRPORT="{airport}"')
    append_bashrc_variables(f'PARTITION="{partition}"')
    append_bashrc_variables(f'REGION="{region}"')
    append_bashrc_variables(f'source /apollo/env/PirateOwlOpsTools/pirate_owl_ops_tools/generate_dto.sh')
    append_bashrc_variables(f'source /apollo/env/PirateOwlOpsTools/pirate_owl_ops_tools/blackmirror_functions.sh')
    append_bashrc_variables(f'source /apollo/env/PirateOwlOpsTools/pirate_owl_ops_tools/help_functions.sh')
    append_zshrc_variables(f'AIRPORT="{airport}"')
    append_zshrc_variables(f'PARTITION="{partition}"')
    append_zshrc_variables(f'REGION="{region}"')
    append_zshrc_variables(f'source /apollo/env/PirateOwlOpsTools/pirate_owl_ops_tools/generate_dto.sh')
    append_zshrc_variables(f'source /apollo/env/PirateOwlOpsTools/pirate_owl_ops_tools/blackmirror_functions.sh')
    append_zshrc_variables(f'source /apollo/env/PirateOwlOpsTools/pirate_owl_ops_tools/help_functions.sh')

    # Append ADC region cert if needed
    if 'us-iso' in region:
        append_bashrc_variables(f'declare -xr AWS_CA_BUNDLE=/etc/pki/{region}/certs/ca-bundle.pem')
        append_bashrc_variables(f'declare -xr REQUEST_CA_BUNDLE=${{AWS_CA_BUNDLE}}')
        append_bashrc_variables(f'declare -xr SSL_CERT_FILE=${{AWS_CA_BUNDLE}}')
        append_zshrc_variables(f'declare -xr AWS_CA_BUNDLE=/etc/pki/{region}/certs/ca-bundle.pem')
        append_zshrc_variables(f'declare -xr REQUEST_CA_BUNDLE=${{AWS_CA_BUNDLE}}')
        append_zshrc_variables(f'declare -xr SSL_CERT_FILE=${{AWS_CA_BUNDLE}}')

    # Loop over users and create/sync home directories if they are in one of the above lists
    for user in user_list:
        try:
            home_directory = f'/home/{user}'
            create_missing_directory(home_directory, owner=user, group='amazon')
            home_path_to_sync = f'{os.path.dirname(os.path.abspath(__file__))}/configuration/directories/home/{user}'
            if os.path.exists(home_path_to_sync):
                symlink_file(home_directory, owner=user, group='amazon')
            else:
                print(f'{user} home directory not managed on host')
        except KeyError:
            print(f'User {user} does not exist on host, skipping')

# This ensures script only executes if called directly
if __name__ == '__main__':
    main()
create_folder_query = '''
	mutation createFolder($name: String!, $visibility: FolderVisibilityEnum) {
        createFolder(input: {name: $name, visibility: $visibility}) {
            ok
            folder {
                pk
                name
                companyPk
                visibility
            }
            error {
                message
                code
            }
        }
    }
'''

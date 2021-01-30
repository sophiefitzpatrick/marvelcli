password_update_query = '''
    mutation updateUserPassword($existingPassword: String!, $newPassword: String!) {
        updateUserPassword(input: {existingPassword: $existingPassword, newPassword: $newPassword}) {
            error {
                message
                code
            }
            ok
        }
     }
'''

user_update_query = '''
	mutation updateCurrentUser($username: String, $email: String, $password: String, $occupation: OccupationEnum) {
        updateCurrentUser(input: {username: $username, email: $email, password: $password, occupation: $occupation}) {
            ok
            user {
                pk
                email
                username
                occupation
            }
            error {
                message
                code
            }
        }
    }
'''

about_user_query = '''
	query myquery {
		user {
			hasPassword
			email
			status
			lastActiveAt
			avatarUrl
			username
			properties {
				enableCommentNotifications
				prototypeProjectsOwnedCount
				userTestProjectsOwnedCount
				screensOwnedCount
				hotspotsOwnedCount
				foldersOwnedCount
				teamsOwnedCount
	        }
		}
	}
'''

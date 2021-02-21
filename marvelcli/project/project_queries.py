delete_project_query = '''
	mutation deleteproject ($pk: Int!) {
		deleteProject(input: {pk: $pk}) {
            ok
        }
    }
'''

create_project_query = '''
	mutation createproject ($name: String!, $password: String!) {
		createProject(input: {name: $name, password: $password}) {
            ok
        }
    }
'''

add_collabs_to_project_query = '''
    mutation addCollaboratorsToProject ($projectPk: Int!, $emails: [String]!){
        addCollaboratorsToProject(input: {projectPk: $projectPk, emails: $emails}) {
            failed {
                email
                message
                code
            }
            succeeded {
                email
            }
            project {
                pk
            }
        }
    }
'''

remove_collabs_from_project_query = '''
    mutation removeCollaboratorsFromProject ($projectPk: Int!, $emails: [String]!){
        removeCollaboratorsFromProject(input: {projectPk: $projectPk, emails: $emails}) {
            failed {
                email
                message
                code
            }
            succeeded
            project {
                pk
            }
        }
    }
'''

get_all_personal_projects_query = '''
    query {
        user {
            projects {
                edges {
                    node {
                        prototypeUrl
                    }
                }
            }
        }
    }
'''

add_groups_to_project_query = '''
    mutation addTeamsToProject($projectPk: Int!, $teamPks: [Int!]!) {
        addTeamsToProject(input: {projectPk: $projectPk, teamPks: $teamPks}) {
            project {
                pk
            }
            succeeded {
                pk
            }
            failed {
                teamPk
                message
                code
            }
            error {
                message
                code
                teamPk
            }
        }
    }
'''

remove_groups_from_project_query = '''
    mutation removeTeamsFromProject($projectPk: Int!, $teamPks: [Int!]!) {
        removeTeamsFromProject(input: {projectPk: $projectPk, teamPks: $teamPks}) {
            project {
                pk
            }
            succeeded {
                pk
            }
            failed {
                teamPk
                message
                code
            }
            error {
                message
                code
                teamPk
            }
        }
    }
'''

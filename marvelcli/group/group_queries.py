delete_groups_query = '''
	mutation deleteGroups($groupPks: [Int!]!) {
        deleteGroups(input: {groupPks: $groupPks}) {
            succeeded
            failed {
                groupPk
                message
                code
            }
            error {
                message
                code
            }
        }
    }
'''

create_group_query = '''
	mutation createTeam($name: String!) {
        createTeam(input: {name: $name}) {
            ok
            team {
                pk
                name
            }
            error {
                message
                code
            }
        }
    }
'''

add_members_query = '''
	mutation addMembersToTeam($teamPk: Int!, $emails: [String]!) {
        addMembersToTeam(input: {teamPk: $teamPk, emails: $emails}) {
            succeeded {
                pk
                email
            }
            failed {
                email
                message
                code
            }
            team {
                members {
                    edges {
                        node {
                            pk
                            email
                        }
                    }
                }
            }
        }
    }
'''

remove_members_query = '''
	mutation removeMembersFromTeam($teamPk: Int!, $emails: [String]!) {
        removeMembersFromTeam(input: {teamPk: $teamPk, emails: $emails}) {
            succeeded
            failed {
                email
                message
                code
            }
            team {
                members {
                    edges {
                        node {
                            pk
                            email
                        }
                    }
                }
            }
        }
    }
'''

update_group_name_query = '''
    mutation updateGroup($pk: Int!, $name: String!) {
        updateGroup(input: {pk: $pk, name: $name}) {
            ok
            error {
                message
                code
            }
            team {
                pk
            }
        }
    }
'''


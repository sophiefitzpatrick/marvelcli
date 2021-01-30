get_billing_info_query = '''
	query user {
  		user {
		  	company {
			    billing {
				    plan {
				    	teamMembers
				        title
				        priceYearly
				        priceMonthly
				    }
				    billingCycle
				    seatQuantityPurchased
				    seatQuantityUsed
				    seats {
				        originallyPurchased
				        payingFor
				        limit
				    }
				    payment
				    projectQuantityUsed
				    nextPaymentDate
				    currency
			    }
			}
		}
	}
'''

invite_users_to_workspace_query = '''
    mutation inviteUsersToWorkspace ($emails: [String!]!, $role: RoleEnum) {
        inviteUsersToWorkspace (input: {emails: $emails, role: $role}) {
            succeeded
            failed {
                email
                message
                code
            }
            error {
                message
                code
                email
            }
        }
    }
'''

remove_users_from_workspace_query = '''
    mutation removeUsersFromWorkspace($emails: [String!]!,) {
        removeUsersFromWorkspace(input: {emails: $emails,}) {
                succeeded
                failed {
                    email
                    message
                    code
                }
                error {
                    message
                    code
                    email
                }
            }
        }
    '''

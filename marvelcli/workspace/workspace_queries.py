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

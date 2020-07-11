Model Architecture Planning

Membership
    -slug
    -type (free, paid)
    -price
    -stripe plan id

UserMembership
    -user (foreign key to default user)
    -stripe customer id
    -membership type (forieign key to membersship)

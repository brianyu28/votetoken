# Voter Token Generation

To facilitate anonymous online voting while protecting against duplicate votes, this application allows registered voters (with a one-time password) to generate a unique token for use in an election. No mapping between users and tokens is stored to protect the anonymity of the election, and each voter's one-time password can only be used to generate a single voting token, to protect against duplicate votes. After votes have been cast, each vote can be checked against the list of authorized tokens to determine whether or not the vote ought to be counted.

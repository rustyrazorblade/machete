
def get_by_email(email) {
    return g.V('email', email)
}
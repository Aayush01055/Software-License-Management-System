def user_context(request):
    # Make the 'user' object available globally
    return {'user': request.user}
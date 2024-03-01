def is_valid_url(url):
    # Check if the URL starts with 'http://' or 'https://'
    if not (url.startswith('http://') or url.startswith('https://')):
        return False

    # Check if there's at least one dot, implying a domain name might be present
    if '.' not in url:
        return False

    # URLs should not contain spaces
    if ' ' in url:
        return False

    return True


url = "https://blackboard.ie.edu/ultra/courses/_79200_1/outline/assessment/_1288267_1/overview/attempt/_2490579_1?courseId=_79200_1"
print(is_valid_url(url))



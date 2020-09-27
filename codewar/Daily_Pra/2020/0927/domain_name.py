def domain_name(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]

#https://www.codewars.com/kata/514a024011ea4fb54200004b/solutions/python
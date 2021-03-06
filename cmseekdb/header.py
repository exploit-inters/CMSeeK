# This file contains all the methods of detecting cms via http Headers
# This is a part of CMSeeK project
# Version: 1.0.0
# Return a list with ['1'/'0','ID of CMS'/'na'] 1 = detected 0 = not detected
def check(h):
    if h == "":
        r = ['0', 'na']
        return r
    else:
        hstring = h
        harray = h.split("\n")

        #### START DETECTION FROM HERE

        if '/wp-json/' in hstring:
            ## WordPress
            r = ['1','wp']

        elif 'X-Drupal-' in hstring or '19 Nov 1978 05' in hstring:
            ## Drupal [the date is interesting isn't it? just google for it ;) ]
            r = ['1', 'dru']

        elif 'Expires: Wed, 17 Aug 2005 00:00:00 GMT' in hstring:
            ## This is the only weird but common header i noticed in joomla Sites
            r = ['1', 'joom']

            
        else:
            r = ['0', 'na']
        return r

from utilityFunctions import *
update_content("/home/fedlix/StaticSite/static","/home/fedlix/StaticSite/public")
generate_pages_recursive("content","template.html","public")
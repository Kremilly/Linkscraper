#!/usr/bin/python3

from core.static.autoload import *

def js_files(url, minify_files, filter_data, download):
    if download:
        download_resources(url, 'js', minify_files, filter_data)
    else:
        start_time = time.time()
        html = session.get(url).content
        soup = bs(html, "html.parser")
    
        Table.header([
            ("Filename", "cyan", True),
            ("URL", "bold blue", False)
        ])

        links = []
        
        for script in soup.find_all("script"):
            if script.attrs.get("src"):
                script_url = urljoin(url, script.attrs.get("src"))
                
                if filter_data:
                    if find(script_url, filter_data):
                        links.append(script_url)
                else:
                    if minify_files:
                        if find(script_url, '.min'):
                            links.append(script_url)
                    else:
                        links.append(script_url)
        
        list_scripts = list(set(links))
        
        for script_url in list_scripts:
            Table.row(get_remote_file_size(script_url), script_url)
        
        end_time = "{:.2f}".format(time.time() - start_time)
        
        Table.caption(f"Total script files on page: {len(list_scripts)} - Time taken: {end_time} seconds")
        Table.display()

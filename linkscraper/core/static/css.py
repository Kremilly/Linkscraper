#!/usr/bin/python3

from core.static.autoload import *

def css_files(url, minify_files, filter_data, download):
    if download:
        download_resources(url, 'css', minify_files, filter_data)
    else:
        start_time = time.time()
        
        html = session.get(url).content
        soup = bs(html, "html.parser")
    
        Table.header([
            ("Filename", "cyan", True),
            ("URL", "bold blue", False)
        ])

        links = []
        
        for css in soup.find_all("link"):
            if css.attrs.get("href"):
                css_url = urljoin(url, css.attrs.get("href"))

                if filter_data:
                    if find(css_url, ".css") and find(css_url, filter_data):
                        links.append(css_url)
                else:
                    if minify_files:
                        if find(css_url, ".css") and find(css_url, ".min.css"):
                            links.append(css_url)
                    else:
                        if find(css_url, ".css"):
                            links.append(css_url)
        
        list_css = list(set(links))
        
        for css_url in list_css:
            Table.row(get_remote_file_size(css_url), css_url)
        
        end_time = "{:.2f}".format(time.time() - start_time)
        
        Table.caption(f"Total CSS files on page: {len(list_css)} - Time taken: {end_time} seconds")
        Table.display()

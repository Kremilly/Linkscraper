#!/usr/bin/python3

from core.static.autoload import *

from utils.date_time import DateTime

class CSS:

    @classmethod
    def css_files(cls, url, *args):
        if args.download:
            return DownloadResources.download(url, 'css', args.minify_files, args.filter_data)
            
        start_time = time.time()
        
        html = session.get(url).content
        soup = bs(html, "html.parser")
    
        Table.header([
            ("Filename", "cyan", True),
            ("URL", "bold blue", False),
            ("Size", "green", False)
        ])

        links = []
        
        for css in soup.find_all("link"):
            if css.attrs.get("href"):
                css_url = urljoin(url, css.attrs.get("href"))

                if css_url.find('.css') != -1:
                    if args.filter_data:
                        if css_url.find(".css") and css_url.find(args.filter_data):
                            links.append(css_url)
                        
                    if args.minify_files:
                        if css_url.find(".css") and css_url.find(".min.css"):
                            links.append(css_url)
                        
                    if css_url.find(".css"):
                        links.append(css_url)
        
        list_css = list(set(links))
        
        for css_url in list_css:
            Table.row(File.get_remote_file_name(css_url), css_url, FileSize.remote_file(css_url))
        
        Table.caption(f"Total CSS files on page: {len(list_css)} - "
                        f"Time taken: {DateTime.calculate_interval(start_time)} seconds")
        
        Table.display()

    @classmethod
    def section(cls, url, minify_files, filter_data, download):
        Layout.header_section("CSS Files")
        cls.css_files(url, minify_files, filter_data, download)

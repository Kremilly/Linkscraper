#!/usr/bin/python3

from core.static.autoload import *

from utils.date_time import DateTime

class JS:

    @classmethod
    def js_files(cls, url, *args):
        if args.download:
            return DownloadResources.download(url, 'js', args.minify_files, args.filter_data)
            
        start_time = time.time()
        html = session.get(url).content
        soup = bs(html, 'html.parser')
    
        Table.header([
            ('Filename', 'cyan', True),
            ('URL', 'bold blue', False),
            ('Size', 'green', False),
        ])

        links = []
        
        for script in soup.find_all('script'):
            if script.attrs.get('src'):
                script_url = urljoin(url, script.attrs.get('src'))
                
                if script_url.find('.js') != -1:
                    if args.filter_data:
                        if script_url.find(args.filter_data):
                            links.append(script_url)
                        
                    if args.minify_files:
                        if script_url.find('.min.js'):
                            links.append(script_url)
                            
                    links.append(script_url)
        
        list_scripts = list(set(links))
        
        for script_url in list_scripts:
            Table.row(File.get_remote_file_name(script_url), script_url, FileSize.remote_file(script_url))
        
        Table.caption(f'Total script files on page: {len(list_scripts)} - '
                        f'Time taken: {DateTime.calculate_interval(start_time)} seconds')
        
        Table.display()

    @classmethod
    def section(cls, url, minify_files, filter_data, download):
        Layout.header_section('Scripts JavaScript')
        cls.js_files(url, minify_files, filter_data, download)

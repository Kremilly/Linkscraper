#!/usr/bin/python3

from core.static.autoload import *

from utils.date_time import DateTime

class Images:

    @classmethod
    def images_files(cls, url, *args):
        if args.download:
            return DownloadResources.download(url, 'images', None, args.filter_data)
            
        start_time = time.time()
        html = session.get(url).content
        soup = bs(html, 'html.parser')
    
        Table.header([
            ('Filename', 'cyan', True),
            ('URL', 'bold blue', False),
            ('Size', 'green', False)
        ])

        links = []
        
        for img in soup.find_all('img'):
            img_url = urljoin(url, img.attrs.get('src'))
            
            if args.filter_data:
                if img_url.find(args.filter_data):
                    links.append(img_url)
            else:
                links.append(img_url)
    
        list_images = list(set(links))
    
        for img_url in list_images:
            Table.row(File.get_remote_file_name(img_url), img_url, FileSize.remote_file(img_url))
        
        Table.caption(f'Total images files on page: {len(list_images)} - '
                      f'Time taken: {DateTime.calculate_interval(start_time)} seconds')
        
        Table.display()

    @classmethod
    def section(cls, url, filter_data, download):
        Layout.header_section('Images')
        cls.images_files(url, filter_data, download)

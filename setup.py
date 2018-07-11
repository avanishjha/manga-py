from __future__ import print_function

from setuptools import setup
from setuptools.command.install import install
from manga_py.meta import __version__, __downloader_uri__, __author__, __email__, __license__
from os import path, system, name


REQUIREMENTS = [
    'lxml',
    'cssselect',
    'Pillow',
    'requests',
    'pycrypto',
    'cfscrape',
    'progressbar2',
    'urllib3',
    'packaging',
    'pyexecjs>=1.5.1',
    'html-purifier',
    'peewee>3.4.0',
]


if path.isfile('requirements.txt'):
    with open('requirements.txt') as f:
        REQUIREMENTS = f.read()


long_description = ''
if path.isfile('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()


release_status = 'Development Status :: 1 - Planning'
# release_status = 'Development Status :: 5 - Production/Stable'
# if ~__version__.find('beta'):
#     release_status = 'Development Status :: 4 - Beta'
# if ~__version__.find('alpha'):
#     release_status = 'Development Status :: 3 - Alpha'


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        if name.find('nt') == -1:
            print('Activate argcomplete')
            system('activate-global-python-argcomplete --user')
            print('Add scripts to .bashrc')
            system('if [ `cat ~/.bashrc | grep python-argcomplete | wc -l` -lt 1 ]; then echo ". ~/.bash_completion.d/python-argcomplete.sh" >> ~/.bashrc; fi')


setup(
    name='manga_py',
    packages=[
        'manga_py',
        'manga_py.cli',
        'manga_py.cli.args',
        'manga_py.libs',
        'manga_py.libs.base',
        'manga_py.libs.crypt',
        'manga_py.libs.http',
        'manga_py.libs.modules',
        'manga_py.libs.modules.html',
        'manga_py.libs.modules.html.templates',
        'manga_py.libs.providers',
    ],
    include_package_data=True,
    version=__version__,
    description='Universal assistant download manga.',
    long_description=long_description,
    author=__author__,
    author_email=__email__,
    url=__downloader_uri__,
    zip_safe=False,
    data_files=[
        # ('manga_py/storage', [
        #     'manga_py/storage/.passwords.json.dist',
        #     'manga_py/storage/.proxy.txt',
        # ]),
    ],
    download_url='{}/archive/{}.tar.gz'.format(__downloader_uri__, __version__),
    keywords=['manga-downloader', 'manga', 'manga-py'],
    license=__license__,
    classifiers=[  # look here https://pypi.python.org/pypi?%3Aaction=list_classifiers
        release_status,
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.5',
    install_requires=REQUIREMENTS,
    cmdclass={
        'install': PostInstallCommand,
    },
    entry_points={
        'console_scripts': [
            'manga-py = manga_py:main',
        ]
    }
)

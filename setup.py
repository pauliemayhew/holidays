from distutils.core import setup


setup(
    name='holidays',
    version='01.',
    author='Maxim Oransky',
    author_email='maxim.oransky@gmail.com',
    packages=[
        'holidays',
    ],
    package_data={
        'holidays': ['data/ru/*'],
    },
    url='https://github.com/shantilabs/holidays',
)
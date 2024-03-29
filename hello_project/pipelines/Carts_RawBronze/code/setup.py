from setuptools import setup, find_packages
setup(
    name = 'Carts_RawBronze',
    version = '1.0',
    packages = find_packages(include = ('carts_rawbronze*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.6.9'],
    entry_points = {
'console_scripts' : [
'main = carts_rawbronze.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)

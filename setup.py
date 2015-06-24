from setuptools import setup

setup(
    name='jjb-artifactory-wrapper',
    version='0.2',
    description='Jenkins Job Builder Artifactory wrapper',
    url='https://github.com/danielredoak/jjb-artifactory-wrapper',
    author="Ryan O'Keeffe",
    author_email='okeefferd@gmail.com',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.wrappers': [
            'artifactory = jjb_artifactory_wrapper.artifactory:artifactory_wrapper']
    },
    packages=['jjb_artifactory_wrapper'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])

jjb-artifactory-wrapper
==================

Jenkins Job Builder Artifactory Wrapper using generic integration.

# Install
```
pip install artifactory.py
```

# Extending
The process is fairly simple.  Manually configure a Jenkins job to enable Artifactory integration adding and configuring the values you want. Use the job xml (available at <Job URL>/config.xml) and compare it to the structure in artifactory.py, modifying as needed.

# Usage
```
wrappers:
  - artifactory:
          artifactory-name: string
          artifactory-url: string
          staging-plugin: string
          deploy-release-repository:
              key-from-text: string
              key-from-select: string
              dynamic-mode: boolean
          deploy-pattern: string
          resolve-pattern: string
          matrix-params: string
          deploy-build-info: boolean
          include-env-vars: boolean
          env-vars-patterns:
              include-patterns: string
              exclude-patterns: string
          discard-old-builds: boolean
          discard-build-artifacts: boolean
          multi-conf-project: boolean
               
```
# Authors
Ryan O'Keeffe (danielredoak)

# Notes

* This is based on the work that xiii did for version 2.2.7 of the plugin (https://github.com/xiii/jenkins-jobs-artifactory), completely re-written for better field name matching, added support for sub-fields, and string casting.
* This is locked at the moment to version of 2.3.0 of jenkins artifactory. Probably would like to make this a variable and perhaps support different fields per version.

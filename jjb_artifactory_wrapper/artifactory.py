import xml.etree.ElementTree as XML


def artifactory_wrapper(parser, xml_parent, data):
    """yaml: artifactory

    Example::
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
    """
    if data is None:
        data = dict()

    notifier = XML.SubElement(xml_parent, 'org.jfrog.hudson.generic.ArtifactoryGenericConfigurator')
    notifier.set('plugin', 'artifactory@2.3.0')

    # details

    details = XML.SubElement(notifier, 'details')

    for opt, attr in (
            ('artifactory-name', 'artifactoryName'),
            ('artifactory-url', 'artifactoryUrl'),
            ('staging-plugin', 'stagingPlugin')
    ):
        XML.SubElement(details, attr).text = data.get(opt, '')

    # details.deployReleaseRepository

    deployreleaserepository = XML.SubElement(details, 'deployReleaseRepository')
    deployreleaserepository_conf = data.get('deploy-release-repository', {})



    for opt, attr in (
            ('key-from-text', 'keyFromText'),
            ('key-from-select', 'keyFromSelect'),
            ('dynamic-mode', 'dynamicMode')
    ):
        value = deployreleaserepository_conf.get(opt, '')
        if isinstance(value, str):
            XML.SubElement(deployreleaserepository, attr).text = value
        else:
            XML.SubElement(deployreleaserepository, attr).text = str(value).lower()


    for opt, attr in (
            ('deploy-pattern', 'deployPattern'),
            ('resolve-pattern', 'resolvePattern'),
            ('matrix-params', 'matrixParams'),
            ('deploy-build-info', 'deployBuildInfo'),
            ('include-env-vars', 'includeEnvVars')
    ):
        value = data.get(opt, '')
        if isinstance(value, str):
            XML.SubElement(notifier, attr).text = value
        else:
            XML.SubElement(notifier, attr).text = str(value).lower()

    # envVarsPatterns

    envvarspatterns = XML.SubElement(notifier, 'envVarsPatterns')
    envvarspatterns_conf = data.get('env-vars-patterns', {})

    for opt, attr in (
            ('include-patterns', 'includePatterns'),
            ('exclude-patterns', 'excludePatterns')
    ):
        XML.SubElement(envvarspatterns, attr).text = envvarspatterns_conf.get(opt, '')

    for opt, attr in (
            ('discard-old-builds', 'discardOldBuilds'),
            ('discard-build-artifacts', 'discardBuildArtifacts'),
            ('multi-conf-project', 'multiConfProject')
    ):
        XML.SubElement(notifier, attr).text = str(data.get(opt, '')).lower()

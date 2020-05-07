version='1.0'
name='api'
namespace=''
docker build  --tag registry.ayomi.fr/$namespace/$name:v$version --build-arg TEST=1 .
docker push registry.ayomi.fr/$namespace/$name:v$version

echo "registry.ayomi.fr/$namespace/$name:v$version"
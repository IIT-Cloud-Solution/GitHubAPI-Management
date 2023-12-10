.\gitapi-env\Scripts\activate

# GitHubAPI-Management
A microservice to fetch different data from the github API

# To Buid the Docker Imahe
docker build -t git-api-flask .

# Add Below Command to CI pipeline
# login to the Dockerhub

docker build -t hiranjanperera/git-api-flask .
docker push hiranjanperera/git-api-flask:latest  

# Run the Docker Image
docker run -p 5001:5001 git-api-flask



# tag the Docker Image
docker tag git-api-flask hiranjanperera/git-api-flask

docker login
docker push hiranjanperera/git-api-flask

# Make sure to start minikube 
minikube start

kubectl apply -f deployment.yml
kubectl get deployments
curl http://localhost/

git-api-flask
kubectl config set-cluster git-api-flask --server=https://your-kubernetes-api-server:6443


# ----------------------- API TESTING 
pip install pytest Flask-Testing requests-mock


cd Downloads
chmod 400 cicd-pipeline.pem
--ec2 ssh command
sudo su
sudo apt update
sudo apt-get upgrade -y

-- adding a github runner

-- setup the docker in ur machine
https://docs.docker.com/engine/install/ubuntu/

docker login 

-- nginex 
sudo apt install nginx

-- find the docker container ip
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 07a2484f2873

cd /etc/nginx/sites-available/
---- add
-- restart nginex
systemctl restart nginx
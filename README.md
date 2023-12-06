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

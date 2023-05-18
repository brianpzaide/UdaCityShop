This repo contains my solution for the capstone project of [Cloud Native Application Architecture nanodegree](https://www.udacity.com/course/cloud-native-application-architecture-nanodegree--nd064)

Todo:

- [x] Use Github Actions to automate the build and push of the Docker images to DockerHub, for all Uda'CityShop microservices.

- [x] Construct declarative Kubernetes manifest to deploy the Uda'CityShop to multiple environments.
    
- [x] Deploy the Uda'CityShop microservices using ArgoCD to the Kubernetes cluster, including dev and prod namespaces.
    
- [x] Apply best security practices and include a short SHA to the new Docker tags. This removes the need to use ```latest``` tag and transitions to a more secure, pinned tag system.
    
- [ ] Use Grafana and Prometheus to construct a dashboard and monitor the Uda'CityShop microservices.

- [x] Rewrite the Ad Service using python and apply best grpc practices.
    
- [x] Construct a Dockerfile for the refactored Ad Service and use Github Actions and ArgoCD to deploy the application to a kubernetes cluster.




<p align="center">
<img src="src/frontend/static/icons/Hipster_HeroLogoCyan.svg" width="300" alt="Online Boutique" />
</p>

This is an application forked from the [GCP Microservice demo](https://github.com/GoogleCloudPlatform/microservices-demo).

**Online Boutique** is a cloud-native microservices demo application.
Online Boutique consists of a 10-tier microservices application. The application is a
web-based e-commerce app where users can browse items,
add them to the cart, and purchase them.

Find **Protocol Buffers Descriptions** at the [`./pb` directory](./pb).

| Service                                              | Language      | Description                                                                                                                       |
| ---------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [frontend](./src/frontend)                           | Go            | Exposes an HTTP server to serve the website. Does not require signup/login and generates session IDs for all users automatically. |                                                       |
| [productcatalogservice](./src/productcatalogservice) | Go            | Provides the list of products from a JSON file and ability to search products and get individual products.                        |
| [currencyservice](./src/currencyservice)             | Node.js       | Converts one money amount to another currency. Uses real values fetched from European Central Bank. It's the highest QPS service. |
| [adservice](./src/adservice)                         | Java          | Provides text ads based on given context words.                                                                                   |

## Deploy
To deploy this application to a Kubernetes cluster use the following command:
```bash
kubectl apply -f kubernetes-manifests/dev/
```
 **Note**: The manifests should be updated to reference existing Docker images for each microservice.

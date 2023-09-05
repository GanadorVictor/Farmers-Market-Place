# Local Farmer Market Platform

## Introduction

The Local Farmer Market Platform is a command-line application that connects local farmers and consumers, facilitating the listing of produce, placing orders, and supporting local agriculture. This README provides essential information for setting up, using, and contributing to the project.

## Problem statement
Many local farmers struggle to reach consumers directly, and consumers often lack convenient access to fresh, locally sourced produce. This disconnect leads to inefficient distribution, higher prices, and limited availability of fresh products.

## solution
The project aims to provide  a digital marketplace where local farmers can list their produce, availability, and prices, and consumers can easily search for and purchase fresh, locally sourced products. This platform aims to bridge the gap between farmers and consumers, enabling direct transactions and supporting local agriculture.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python (version 3.6 or higher)
- Pipenv (for managing virtual environments)

### Installation

1. **Clone the repository:**

   git clone <repository-url> <br/>
   cd farmersMarketplace

2. **Set up a virtual environment using Pipenv:**

   pipenv install

3. **Activate the virtual environment:**

   pipenv shell

### Usage
1. **Creating Farmer Profiles** </br>
To create a farmer profile:

python cli.py create-farmer</br>
Follow the prompts to provide your name, contact information, and farm details.

2. **Listing Produce** </br>
To list your produce as a farmer:

python cli.py add-produce </br>
Follow the prompts to add product details, including name, description, and price.

3. **Placing Orders** </br>
To place an order as a consumer:

python cli.py place-order </br>
Follow the prompts to select the product you want and provide your name.

4. **Viewing Orders** </br>
To view your orders as a farmer: </br>

python cli.py list-orders</br> 
This will display a list of orders placed by consumers for your produce.

## Contributing
Contributions to our project are highly encouraged and welcome! If you'd like to contribute, please follow these steps:

1. **Fork the Repository.**

2. **Create a New Branch for Your Feature or Bug Fix:**

## Contact Details
For any inquiries, please reach out to

judysigilai75@gmail.com


## License
This project is licensed under the MIT License. For details, see the LICENSE.md file.

Thank you for contributing to the Local Farmer Market Platform, and we look forward to growing our community of local farmers and consumers together!
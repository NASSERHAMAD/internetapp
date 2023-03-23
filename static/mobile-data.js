var mobiles = [
    {
      "id": 1,
      "brand": "Apple",
      "model": "iPhone 12","price": 799,
      "image": "https://fakeimg.pl/300x200/"
      },
      {
      "id": 2,
      "brand": "Samsung",
      "model": "Galaxy S21",
      "price": 699,
      "image": "https://fakeimg.pl/300x200/"
      },
      {
      "id": 3,
      "brand": "OnePlus",
      "model": "8T",
      "price": 599,
      "image": "https://fakeimg.pl/300x200/"
      },
      {
      "id": 4,
      "brand": "Google",
      "model": "Pixel 5",
      "price": 699,
      "image": "https://fakeimg.pl/300x200/"
      },
      {
      "id": 5,
      "brand": "Xiaomi",
      "model": "Mi 11",
      "price": 699,
      "image": "https://fakeimg.pl/300x200/"
      }
      ];
      
      var mobilesContainer = document.querySelector("#mobiles-container");
      
      for (var i = 0; i < mobiles.length; i++) {
      var mobile = mobiles[i];
      
      var card = document.createElement("div");
      card.classList.add("card");
      
      var image = document.createElement("img");
      image.classList.add("card-img-top");
      image.setAttribute("src", mobile.image);
      
      var cardBody = document.createElement("div");
      cardBody.classList.add("card-body");
      
      var title = document.createElement("h5");
      title.classList.add("card-title");
      title.textContent = mobile.brand + " " + mobile.model;
      
      var price = document.createElement("p");
      price.classList.add("card-text");
      price.textContent = "$" + mobile.price;
      
      cardBody.appendChild(title);
      cardBody.appendChild(price);
      
      card.appendChild(image);
      card.appendChild(cardBody);
      
      mobilesContainer.appendChild(card);
      }

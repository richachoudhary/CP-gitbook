# Amazon ShoppingCart



## 1. Requirement Gathering

### 1.1 FRs

* users can add/update/remove items in cart
* only registered users can create cart
* save cart item in DB
* Update cart amount on item added in art
* Calculate total price
* unpurchased items continue to stay in cart until bought
* once purchased; items should get removed from cart
* \[?] apply some discount offer/promo code to card while checkout
* \[?] one user can have single cart only
* \[?] restrict user can not add more than 10 same items in cart

### 1.2 NFRs

* High Consistency - added items should be immediately visible
* High Durability - added items should not be lost
* Good Availability (can be compromised according to `CAP`)
* System should scale-up with increase in userbase

### 1.3 Out Of Scopes

* send notification to user that item going to be out of stock
* remove item if item is removed from inventory and message and mail to user
* Items recommendation
* User Analytics

## 2. BOTEC

### 2.1 Scale of System

* Total users: 1B
* DAU: 100M (very low % because; avg customer behavior: "Buy Now" & not "Add to Cart")
* read:write :: 10:1

### 2.2 Storage size estimation

* things to store: links + product\_info + cart\_item\_meta
  * \=> link: 500 bytes
  * \=> product\_info: 1 kb
  * \=> cart\_item\_meta: 1kb
  * \==> TOTAL: 2.5kb
* daily size reqd: 2.5kb \* 100M = 0.25 G\*M = 0.25TB
* in a year(assume auto-cleanup) = 365 \* 0.25TB = 91.25TB = \~100TB

## 3. APIs

* signup()
* login()
* logout()
* getCartItems(user\_token)
* addItemToCart(user\_token, product\_id, quantity) -> item\_id(in cart) & product\_id(in catalogue)
* upateItemInCart(user\_token, item\_id, new\_quantity) # call `removeItemFromCart()` is new\_quantity == 0
* removeItemFromCart(user\_token, item\_id)
* pruneCart(user\_token)

## 4. Tables

![](<../../.gitbook/assets/Screenshot 2021-11-14 at 9.26.09 PM.png>)

![](<../../.gitbook/assets/Screenshot 2021-11-14 at 9.24.01 PM.png>)

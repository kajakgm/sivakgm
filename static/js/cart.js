var updateBtns = document.getElementsByClassName('update-cart')

    for (i = 0; i < updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
            console.log(updateBtns);
            var productId = this.dataset.product
            var action = this.dataset.action
            //console.log('productId:', productId, 'Action:', action);
            //console.log('USER:', user);
            console.log('hello');
            if (user == 'AnonymousUser'){
                console.log('User is not authenticated');
            }else{
                updateUserOrder(productId, action)
      }
    })}
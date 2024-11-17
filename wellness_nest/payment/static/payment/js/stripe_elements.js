/*
    core logic/payment flow for this comes from :
    http://stripe.com/docs/payments/accept-a-payment

    https://stripe.com/docs/stripe-js

*/ 

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripePublicKey);
console.log(stripe)
var elements = stripe.elements();
var style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};
var card = elements.create('card', {style: style});

card.mount('#card-element');

//handling realtime errors on card element

card.addEventListener('change',function(event) {
    var  errorDiv = document.getElementById('card-errors');
    if(event.error){
        var html = `
            <span classs="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${ event.error.message }</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submission

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    //Disable card data field to prevent chnages during payment processing.
    $('#submit-button').attr('disabled', true);
    //Triggers the form to spade out when user clicks check out
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }// gives the payment method and then execute the function insid then
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
                //Error message to display when card payment fails or wrong info
            $(errorDiv).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            //Enabling card data field to correct the details after error.
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});


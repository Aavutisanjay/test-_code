from flask import Flask, render_template,request,session
app = Flask(__name__)
app.secret_key='automotive_store'
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/products')
def products():
    return render_template('products.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/engine-parts')
def engine_parts():
    return render_template('engine_parts.html')
@app.route('/electrical_parts')
def electrical_parts():
    return render_template('electrical_parts.html')
@app.route('/brake_system')
def brake_system():
    return render_template('brake_system.html')
@app.route('/suspension_parts')
def suspension_parts():
    return render_template('suspension_parts.html')
@app.route('/tyres&wheels')
def tyres_wheels():
    return render_template('tyres&wheels.html')
@app.route('/lighting')
def lighting():
    return render_template('lighting.html')
@app.route('/filter')
def filter():
    return render_template('filter.html')
@app.route('/interior_accessories')
def interior_accessories():
    return render_template('interior_accessories.html')
@app.route('/exterior_accessories')
def exterior_accessories():
    return render_template('exterior_accessories.html')
@app.route('/cooling_system')
def cooling_system():
    return render_template('cooling_system.html')
@app.route('/exhaust_system')
def exhaust_system():
    return render_template('exhaust_system.html')
@app.route('/safety_security')
def safety_security():
    return render_template('safety_security.html')
@app.route('/cart',methods=['GET','POST'])
def cart():
    if request.method == 'POST':
        product_id = request.form['product_id']
        product_name = request.form['product_name']
        price = request.form['price']
        image = request.form['image']
        #create cart if it does not exist
        if 'cart' not in session:
            session['cart'] = []
        product_found = False
        for item in session['cart']:
            if item ['name'] == product_name:
                item['quantity'] += 1
                product_found = True
                break
        # if product exist in the cart
        if not product_found:
         session['cart'].append({
            'id':product_id,
            'name':product_name,
            'price':int(price),
            'quantity': 1,
            'image':image
        })
        session.modified=True
        #debugging output
        print(session['cart'])
        print("Cart Route Executed")
        print("Current Session:",session.get('cart'))
    #calculation total
    total =0
    for item in session.get('cart',[]):
        total += item['price'] * item['quantity']
        #calculation cart badge count
    cart_count = 0
    for item in session.get('cart',[]):
        cart_count += item['quantity']
    return render_template(
        'cart.html',
        cart_items=session.get('cart',[]),
        total=total,
    )
if __name__ ==  '__main__':
    app.run(debug=True)
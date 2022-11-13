def item(request, id_item):

    form_data = request.POST
    if request.method == "POST":

    else: None

        tastes_form = TasteForm(form_data)
        product = Product.objects.get(id=id_item)
        context	= {'product': product, 'form_taste':tastes_form}

            if	request.method	!=	"POST"	or	not tastes_form.is_valid():

            return render(request, "catalog/item.html",context)

            user_id = User.objects.get(id=request.user.id)
            num = Order.objects.order_by('number').last()
                if num is None:
                    num = 1
                elif num.status == '0':
                    num = num.number
                else:

                    num = num.number + 1
                    order_id = Order.objects.get_or_create(id_user=user_id,	status='0', number=num)
                    order_comp = OrderComposition.objects.filter(id_order=order_id[0], id_product=id_item)
                        if order_comp.count() != 0:

                            order_comp=OrderComposition.objects.get(id_orde r=order_id[0], id_product=id_item) order_comp.quantity+=tastes_form.cleaned_data['quant ity']
                            order_comp.save()

                        else:

                            OrderComposition.objects.create(id_order=order_id[0], price=product.price,id_product=product,**tastes_form.cleaned_d ata)
                            return render(request, 'catalog/succesful_add.html', {'product': product})

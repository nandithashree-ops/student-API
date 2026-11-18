const express = require("express");
const app = express();
app.use(express.json());
let orders=[];
app.post("/addOrders",(req,res)=>{
    const order = {
        id:orders.length+1,
        product:req.body.product,
        quantity:req.body.quantity,
        price:req.body.price
    };
    orders.push(orders);
    res.json({
        message:"Order added successfully",
        order:order
    });
});
app.get("/showOrders",(req,res)=>{
    res.json({
        message:"Recent Orders",
        orders:orders.slice().reverse()
    });
});
app.listen(3000,()=>{
    console.log("Server running on port 3000");
});

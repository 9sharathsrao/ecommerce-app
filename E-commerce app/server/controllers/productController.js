const getProducts = (req, res) => {
    res.status(200).json({ message: "List of products" });
};

const addProduct = (req, res) => {
    const { name, price } = req.body;
    res.status(201).json({ message: `Product ${name} added with price ${price}` });
};

module.exports = { getProducts, addProduct };
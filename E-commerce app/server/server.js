const express = require('express');
const productRoutes = require('./routes/productRoutes');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use('/api', productRoutes);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
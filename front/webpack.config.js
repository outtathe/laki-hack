const webpack = require('webpack');
const path_to_static_js = '/static/js'
const config = {
    entry: {
        "/public/js/index": [__dirname + '/src/index.tsx'],
        "/bot/js/index": [__dirname + '/src/bot_index.tsx'],
        "/admin/js/index": [__dirname + '/src/admin_index.tsx'],
    },
    output: {
        path: __dirname + '',
        filename: '[name].js'
    },
    resolve: {
        extensions: ['.js', /*'.jsx',*/ '.tsx', '.css']
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
            },
            {
                test: /\.s[ac]ss$/i,
                use: [
                    // Creates `style` nodes from JS strings
                    "style-loader",
                    // Translates CSS into CommonJS
                    "css-loader",
                    // Compiles Sass to CSS
                    "sass-loader",
                ],
            },
            {
                test: /\.jsx?/,
                exclude: /node_modules/,
                use: 'babel-loader',
            },
            {
                test: /\.tsx?$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
            },
            {
                test: /\.js$/,
                use: ["source-map-loader"],
                enforce: "pre"
            },
        ],
    },
    mode: 'development'
};
module.exports = config;
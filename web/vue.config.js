module.exports = {
    chainWebpack: config => {
        config.module.rules.delete('eslint');
    },
    pages: {
        home: {
            entry: 'src/home/main.js',
            template: 'public/index.html',
            filename: 'home.html',
            title: 'Home Page',
            chunks: ['chunk-vendors', 'chunk-common', 'home']
        },
        user: {
            entry: 'src/user/main.js',
            template: 'public/index.html',
            filename: 'user.html',
            title: 'User Page',
            chunks: ['chunk-vendors', 'chunk-common', 'user']
        }
    },
    assetsDir: 'vstatic',
    configureWebpack: {
        devtool: 'source-map',
    },
    devServer: {
        index: 'home.html',
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:5000/api/',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''
                }
            },
            '/user': {
                target: 'http://127.0.0.1:8080/user.html/',
                changeOrigin: false,
                pathRewrite: {
                    '^/user': ''
                }
            }
        }
    },
    outputDir: '../vtemplates'
}
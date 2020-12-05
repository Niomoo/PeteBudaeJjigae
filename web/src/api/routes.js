import Request from '../http-request'

export const findAllViewPoints = (userInput) => {
    return Request({
        url: 'findAllViewPoints/' + userInput,
        method: 'GET'
    })
}

export const nearestViewpoint = (lng, lat) => {
    return Request({
        url: '/findNearestViewpoint/' + lng + '&' + lat,
        method: 'GET'
    })
}

export const firstRecommend = (start, inputTags) => {
    return Request({
        url: '/firstRecommend/' + start + '&' + inputTags,
        method: 'GET'
    })
}

export const changePoint = (changeIndex, change) => {
    return Request({
        url: '/changePoint/' + changeIndex + '&' + change,
        method: 'GET'
    })
}

export const addPoint = (addIndex) => {
    return Request({
        url: '/addPoint/' + addIndex,
        method: 'GET'
    })
}


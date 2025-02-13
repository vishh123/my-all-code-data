function areaOfRectangle (length, width) {
    return length*width
}

function areaOfCircle (radius) {
return Math.PI * Math.pow(radius, 2)
}

function areaOfTriangle (base, height) {
    return 0.5*base*height
}

function calculatePaintingCost(dimension1, dimention2, calculateArea) {
   const area = calculateArea(dimension1,dimention2)

   const costPerUnit = 2
   const totalCost = area * costPerUnit

    return totalCost

}

console.log( calculatePaintingCost(5, 10, areaOfRectangle));

console.log( calculatePaintingCost(3, null, areaOfCircle));

console.log( calculatePaintingCost(6, 8, areaOfTriangle));


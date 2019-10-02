// https://www.codewars.com/kata/highest-and-lowest


const londonCityHacker = (journey) => {
    const tube_cost = 2.40;
    const bus_cost = 1.50;
    return `£${journey
        .reduce((accumulator, currentValue) => {
            if (typeof currentValue === 'string') {
                accumulator.push(tube_cost);
            } else if (typeof currentValue === 'number') {
                if (accumulator.slice(-1)[0] !== undefined && accumulator.slice(-1)[0] === bus_cost) {
                    accumulator.push(0.0);
                } else {
                    accumulator.push(bus_cost);
                }
            } else {
                throw new Error(`Whoops! ${typeof currentValue} ${currentValue}`);
            }
            return accumulator;
        }, [])
        .reduce((a, b) => a + b, 0.0)
        .toFixed(2)}`
};

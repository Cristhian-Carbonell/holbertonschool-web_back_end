class Widget {
    constructor() {
        if (this.constructor === Widget) {
            throw new TypeError('Abstract class "Widget" cannot be instantiated directly.'); 
        }

        if (this.schema === undefined) {
            throw new TypeError('Classes extending the widget abstract class');
        }
    }
}

class PieChart extends Widget {
    constructor() {
        super();
    }

    get schema() {
        return {
            "name": "PIE_CHART",
            "data": []
        }
    }
}

new PieChart();
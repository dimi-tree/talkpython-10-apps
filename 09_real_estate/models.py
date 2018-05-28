class Purchase:

    def __init__(self, street, city, zip, state, beds, baths, sq__ft, home_type, sale_date, price, latitude, longitude):
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.beds = beds
        self.baths = baths
        self.sq__ft = sq__ft
        self.home_type = home_type
        self.sale_date = sale_date
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def create_from_dict(d):
        return Purchase(
            d['street'],
            d['city'],
            d['zip'],
            d['state'],
            int(d['beds']),
            int(d['baths']),
            int(d['sq__ft']),
            d['type'],
            d['sale_date'],
            float(d['price']),
            float(d['latitude']),
            float(d['longitude']),
        )

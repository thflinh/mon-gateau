from pymongo import MongoClient
import sys

MONGO_URI = "mongodb+srv://ptlinhuni_db_user:%40Linhxinh03@cake-db.jouzhcp.mongodb.net/?appName=cake-db"

client = MongoClient(MONGO_URI)
db = client["cakedb"]
collection = db["cakes"]

# Only clear the collection if --reset is passed (keeps your added cakes when you just restart the app)
RESET = "--reset" in sys.argv

cakes = [
    {
        "name": "Classic Chocolate Cake",
        "image": "/static/images/classic-choco.jpg",
        "description": "A rich, moist chocolate cake with velvety chocolate buttercream frosting. This is the ultimate crowd-pleaser for any chocolate lover.",
        "category": "Chocolate",
        "difficulty": "Medium",
        "prep_time": "30 min",
        "bake_time": "35 min",
        "servings": 12,
        "ingredients": [
            "2 cups all-purpose flour",
            "2 cups sugar",
            "3/4 cup unsweetened cocoa powder",
            "2 teaspoons baking soda",
            "1 teaspoon salt",
            "2 eggs",
            "1 cup buttermilk",
            "1 cup hot water",
            "1/2 cup vegetable oil",
            "2 teaspoons vanilla extract"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease and flour two 9-inch round cake pans.",
            "In a large bowl, whisk together flour, sugar, cocoa powder, baking soda, and salt.",
            "Add eggs, buttermilk, oil, and vanilla. Beat with a mixer on medium speed for 2 minutes.",
            "Stir in hot water — the batter will be thin, and that's perfectly normal.",
            "Pour batter evenly into prepared pans.",
            "Bake for 30-35 minutes, or until a toothpick inserted in the center comes out clean.",
            "Cool in pans for 10 minutes, then transfer to a wire rack to cool completely.",
            "Frost with chocolate buttercream and serve."
        ]
    },
    {
        "name": "Strawberry Shortcake",
        "image": "/static/images/strawberry-short.jpg",
        "description": "Light, fluffy biscuits layered with fresh strawberries and clouds of whipped cream. A timeless summer dessert.",
        "category": "Fruit",
        "difficulty": "Easy",
        "prep_time": "20 min",
        "bake_time": "15 min",
        "servings": 8,
        "ingredients": [
            "2 cups all-purpose flour",
            "1/3 cup sugar",
            "1 tablespoon baking powder",
            "1/4 teaspoon salt",
            "1/2 cup cold butter, cubed",
            "2/3 cup milk",
            "1 egg",
            "4 cups fresh strawberries, sliced",
            "1/4 cup sugar (for strawberries)",
            "2 cups heavy whipping cream",
            "3 tablespoons powdered sugar"
        ],
        "steps": [
            "Preheat oven to 425°F (220°C).",
            "Toss sliced strawberries with 1/4 cup sugar and refrigerate for 30 minutes.",
            "Mix flour, sugar, baking powder, and salt. Cut in cold butter until crumbly.",
            "Whisk milk and egg together, then stir into flour mixture just until combined.",
            "Drop dough onto a baking sheet in 8 mounds.",
            "Bake for 12-15 minutes until golden brown.",
            "Whip heavy cream with powdered sugar until stiff peaks form.",
            "Split biscuits, layer with strawberries and whipped cream. Serve immediately."
        ]
    },
    {
        "name": "Red Velvet Cake",
        "image": "/static/images/red-velvet.jpg",
        "description": "A stunning deep-red cake with a subtle cocoa flavor, topped with tangy cream cheese frosting. Perfect for celebrations.",
        "category": "Classic",
        "difficulty": "Medium",
        "prep_time": "25 min",
        "bake_time": "30 min",
        "servings": 14,
        "ingredients": [
            "2 1/2 cups all-purpose flour",
            "1 1/2 cups sugar",
            "1 teaspoon cocoa powder",
            "1 teaspoon baking soda",
            "1 teaspoon salt",
            "2 eggs",
            "1 1/2 cups vegetable oil",
            "1 cup buttermilk",
            "2 tablespoons red food coloring",
            "1 teaspoon vanilla extract",
            "1 teaspoon white vinegar",
            "16 oz cream cheese (for frosting)",
            "1/2 cup butter, softened (for frosting)",
            "4 cups powdered sugar (for frosting)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease and flour three 9-inch round pans.",
            "Whisk flour, sugar, cocoa, baking soda, and salt in a large bowl.",
            "In another bowl, mix eggs, oil, buttermilk, food coloring, vanilla, and vinegar.",
            "Combine wet and dry ingredients, mixing until just smooth.",
            "Divide batter evenly among the three pans.",
            "Bake for 25-30 minutes until a toothpick comes out clean.",
            "Cool completely on wire racks.",
            "For frosting: beat cream cheese and butter until smooth, then gradually add powdered sugar.",
            "Frost between layers, on top, and around the sides. Refrigerate before serving."
        ]
    },
    {
        "name": "New York Cheesecake",
        "image": "/static/images/ny-cheesecake.jpg",
        "description": "Dense, creamy, and impossibly smooth. This classic New York-style cheesecake has a buttery graham cracker crust and a rich filling.",
        "category": "Cheesecake",
        "difficulty": "Hard",
        "prep_time": "30 min",
        "bake_time": "60 min",
        "servings": 12,
        "ingredients": [
            "2 cups graham cracker crumbs",
            "1/4 cup sugar",
            "1/2 cup melted butter",
            "32 oz cream cheese, softened",
            "1 cup sugar",
            "5 eggs",
            "2 teaspoons vanilla extract",
            "1/4 cup all-purpose flour",
            "1 cup sour cream"
        ],
        "steps": [
            "Preheat oven to 325°F (160°C). Wrap the outside of a 9-inch springform pan with aluminum foil.",
            "Mix graham cracker crumbs, sugar, and melted butter. Press firmly into the bottom of the pan.",
            "Bake crust for 10 minutes, then let it cool.",
            "Beat cream cheese and sugar until smooth — do not over-beat or it will crack.",
            "Add eggs one at a time, mixing on low after each.",
            "Stir in vanilla, flour, and sour cream until just combined.",
            "Pour filling onto cooled crust.",
            "Place springform pan in a larger pan, pour hot water halfway up the sides (water bath).",
            "Bake for 55-60 minutes until edges are set but center jiggles slightly.",
            "Turn off oven, crack the door, and let cheesecake cool inside for 1 hour.",
            "Refrigerate for at least 4 hours (overnight is best) before serving."
        ]
    },
    {
        "name": "Carrot Cake",
        "image": "/static/images/carrot.jpg",
        "description": "A warmly spiced cake loaded with fresh carrots, walnuts, and topped with luscious cream cheese frosting.",
        "category": "Classic",
        "difficulty": "Medium",
        "prep_time": "25 min",
        "bake_time": "40 min",
        "servings": 12,
        "ingredients": [
            "2 cups all-purpose flour",
            "2 teaspoons baking soda",
            "2 teaspoons cinnamon",
            "1/2 teaspoon nutmeg",
            "1/2 teaspoon salt",
            "1 1/2 cups vegetable oil",
            "2 cups sugar",
            "4 eggs",
            "3 cups finely grated carrots",
            "1 cup chopped walnuts",
            "1/2 cup crushed pineapple, drained",
            "8 oz cream cheese (for frosting)",
            "1/4 cup butter (for frosting)",
            "2 cups powdered sugar (for frosting)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease two 9-inch round pans.",
            "Whisk flour, baking soda, cinnamon, nutmeg, and salt together.",
            "In a separate bowl, beat oil, sugar, and eggs until well combined.",
            "Gradually add dry ingredients to wet ingredients.",
            "Fold in grated carrots, walnuts, and pineapple.",
            "Divide batter between pans and bake for 35-40 minutes.",
            "Cool completely before frosting.",
            "Beat cream cheese and butter, then gradually add powdered sugar for the frosting.",
            "Frost the cake and garnish with extra walnuts."
        ]
    },
    {
        "name": "Lemon Drizzle Cake",
        "image": "/static/images/lemon-drizzle.jpg",
        "description": "A bright, zesty cake soaked in a sweet lemon syrup with a crunchy sugar glaze on top. Perfect with afternoon tea.",
        "category": "Citrus",
        "difficulty": "Easy",
        "prep_time": "15 min",
        "bake_time": "35 min",
        "servings": 10,
        "ingredients": [
            "1 3/4 cups all-purpose flour",
            "2 teaspoons baking powder",
            "1/2 teaspoon salt",
            "3/4 cup sugar",
            "3 eggs",
            "3/4 cup butter, melted",
            "1/2 cup milk",
            "Zest of 2 lemons",
            "Juice of 2 lemons (for drizzle)",
            "1/2 cup granulated sugar (for drizzle)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease and line a 9x5 loaf pan.",
            "Whisk flour, baking powder, and salt together.",
            "In another bowl, beat sugar, eggs, melted butter, milk, and lemon zest.",
            "Fold dry ingredients into wet until just combined.",
            "Pour into prepared pan and bake for 30-35 minutes.",
            "While cake bakes, mix lemon juice and sugar for the drizzle.",
            "When cake comes out, poke holes all over with a skewer.",
            "Pour the lemon drizzle over the warm cake and let it soak in.",
            "Cool in pan before slicing."
        ]
    },
    {
        "name": "Tiramisu",
        "image": "/static/images/tiramisu.jpg",
        "description": "An elegant Italian no-bake dessert with layers of espresso-soaked ladyfingers and rich mascarpone cream, dusted with cocoa.",
        "category": "Italian",
        "difficulty": "Medium",
        "prep_time": "30 min",
        "bake_time": "No bake (chill 4+ hrs)",
        "servings": 9,
        "ingredients": [
            "6 egg yolks",
            "3/4 cup sugar",
            "16 oz mascarpone cheese",
            "2 cups heavy whipping cream",
            "2 cups strong espresso, cooled",
            "2 tablespoons coffee liqueur (optional)",
            "1 package ladyfinger biscuits (~24)",
            "Unsweetened cocoa powder for dusting"
        ],
        "steps": [
            "Whisk egg yolks and sugar until thick and pale yellow (about 4 minutes).",
            "Add mascarpone to the egg yolk mixture and beat until smooth.",
            "In a separate bowl, whip heavy cream to stiff peaks.",
            "Gently fold whipped cream into the mascarpone mixture.",
            "Combine cooled espresso and coffee liqueur in a shallow dish.",
            "Quickly dip each ladyfinger into the espresso — don't soak them.",
            "Layer dipped ladyfingers in the bottom of a 9x9 dish.",
            "Spread half the mascarpone cream over the ladyfingers.",
            "Repeat with another layer of dipped ladyfingers and remaining cream.",
            "Cover and refrigerate for at least 4 hours (overnight is best).",
            "Dust generously with cocoa powder right before serving."
        ]
    },
    {
        "name": "Banana Bread",
        "image": "/static/images/banana-bread.jpg",
        "description": "Ultra-moist banana bread with a golden crust. The riper the bananas, the better the flavor. A comfort food classic.",
        "category": "Quick Bread",
        "difficulty": "Easy",
        "prep_time": "15 min",
        "bake_time": "60 min",
        "servings": 10,
        "ingredients": [
            "3 ripe bananas, mashed",
            "1/3 cup melted butter",
            "3/4 cup sugar",
            "1 egg, beaten",
            "1 teaspoon vanilla extract",
            "1 teaspoon baking soda",
            "Pinch of salt",
            "1 1/2 cups all-purpose flour",
            "1/2 cup walnuts or chocolate chips (optional)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease a 9x5 loaf pan.",
            "Mash bananas in a bowl with a fork until smooth.",
            "Mix in melted butter, sugar, egg, and vanilla.",
            "Sprinkle in baking soda and salt, then stir in flour until just combined.",
            "Fold in walnuts or chocolate chips if using.",
            "Pour batter into prepared pan.",
            "Bake for 55-60 minutes until a toothpick comes out clean.",
            "Let cool in pan for 10 minutes, then transfer to a wire rack."
        ]
    },
    {
        "name": "Chocolate Lava Cake",
        "image": "/static/images/choco-lava.jpg",
        "description": "Individual cakes with a warm, gooey molten chocolate center that flows out when you cut into them. Impressive yet surprisingly easy.",
        "category": "Chocolate",
        "difficulty": "Medium",
        "prep_time": "15 min",
        "bake_time": "14 min",
        "servings": 4,
        "ingredients": [
            "4 oz semi-sweet chocolate",
            "1/2 cup butter",
            "1 cup powdered sugar",
            "2 eggs",
            "2 egg yolks",
            "6 tablespoons all-purpose flour",
            "Butter and cocoa for ramekins"
        ],
        "steps": [
            "Preheat oven to 425°F (220°C). Butter four 6-oz ramekins and dust with cocoa powder.",
            "Melt chocolate and butter together in a microwave (30-second intervals, stirring each time).",
            "Stir in powdered sugar until smooth.",
            "Whisk in eggs and egg yolks.",
            "Fold in flour until just combined — don't overmix.",
            "Divide batter among ramekins.",
            "Bake for exactly 12-14 minutes — edges should be firm but center soft.",
            "Let sit for 1 minute, then invert onto plates.",
            "Serve immediately with vanilla ice cream or whipped cream."
        ]
    },
    {
        "name": "Japanese Cotton Cheesecake",
        "image": "/static/images/cotton-cheesecake.jpg",
        "description": "An incredibly light, jiggly cheesecake that melts in your mouth. Think of it as a cloud made of cheesecake.",
        "category": "Cheesecake",
        "difficulty": "Hard",
        "prep_time": "30 min",
        "bake_time": "60 min",
        "servings": 8,
        "ingredients": [
            "8 oz cream cheese, softened",
            "1/4 cup butter",
            "1/2 cup milk",
            "1/3 cup all-purpose flour",
            "2 tablespoons cornstarch",
            "6 egg yolks",
            "6 egg whites",
            "1/2 cup sugar",
            "1/4 teaspoon cream of tartar",
            "1 teaspoon vanilla extract",
            "1 tablespoon lemon juice"
        ],
        "steps": [
            "Preheat oven to 320°F (160°C). Line the bottom of a 9-inch round pan with parchment.",
            "Melt cream cheese, butter, and milk together over low heat, stirring until smooth.",
            "Remove from heat. Sift in flour and cornstarch, stir until smooth.",
            "Add egg yolks one at a time, mixing well after each. Stir in vanilla and lemon juice.",
            "In a separate bowl, beat egg whites and cream of tartar until foamy.",
            "Gradually add sugar while beating until stiff, glossy peaks form.",
            "Fold 1/3 of the meringue into the cheese mixture to lighten it.",
            "Gently fold in the remaining meringue in two batches — do NOT deflate it.",
            "Pour into prepared pan. Place pan in a larger pan with hot water (water bath).",
            "Bake for 55-60 minutes until golden and the center barely jiggles.",
            "Turn off oven, crack the door, and let cool inside for 30 minutes.",
            "Refrigerate for 2 hours before serving."
        ]
    },
    {
        "name": "Funfetti Birthday Cake",
        "image": "/static/images/funfetti.jpg",
        "description": "A cheerful vanilla cake loaded with rainbow sprinkles and topped with fluffy vanilla buttercream. Pure birthday joy.",
        "category": "Birthday",
        "difficulty": "Easy",
        "prep_time": "20 min",
        "bake_time": "28 min",
        "servings": 14,
        "ingredients": [
            "2 1/2 cups all-purpose flour",
            "2 cups sugar",
            "1 tablespoon baking powder",
            "1 teaspoon salt",
            "1 cup butter, softened",
            "4 egg whites",
            "1 cup milk",
            "2 teaspoons vanilla extract",
            "1/2 teaspoon almond extract",
            "3/4 cup rainbow sprinkles",
            "1 cup butter, softened (for frosting)",
            "4 cups powdered sugar (for frosting)",
            "3 tablespoons heavy cream (for frosting)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease and flour two 9-inch round pans.",
            "Whisk flour, sugar, baking powder, and salt together.",
            "Add softened butter and mix until crumbly.",
            "Beat in egg whites, milk, vanilla, and almond extract until fluffy (about 2 minutes).",
            "Gently fold in sprinkles by hand.",
            "Divide batter between pans and bake for 25-28 minutes.",
            "Cool completely before frosting.",
            "For frosting: beat butter until pale, gradually add powdered sugar and cream.",
            "Frost the cake and cover with more sprinkles!"
        ]
    },
    {
        "name": "Matcha Green Tea Cake",
        "image": "/static/images/matcha.jpg",
        "description": "An earthy, subtly sweet Japanese-inspired cake with vibrant green color and a delicate white chocolate cream cheese frosting.",
        "category": "Specialty",
        "difficulty": "Medium",
        "prep_time": "25 min",
        "bake_time": "30 min",
        "servings": 12,
        "ingredients": [
            "2 cups all-purpose flour",
            "3 tablespoons matcha green tea powder",
            "2 teaspoons baking powder",
            "1/2 teaspoon salt",
            "3/4 cup butter, softened",
            "1 1/2 cups sugar",
            "4 eggs",
            "1 cup milk",
            "1 teaspoon vanilla extract",
            "4 oz white chocolate, melted (for frosting)",
            "8 oz cream cheese (for frosting)",
            "2 cups powdered sugar (for frosting)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease two 8-inch round pans.",
            "Sift flour, matcha powder, baking powder, and salt together. Sifting is critical for matcha to avoid clumps.",
            "Cream butter and sugar until light and fluffy.",
            "Add eggs one at a time, beating well after each.",
            "Alternate adding dry ingredients and milk, starting and ending with dry.",
            "Stir in vanilla extract.",
            "Divide batter between pans and bake for 28-30 minutes.",
            "Cool completely.",
            "For frosting: beat cream cheese until smooth, mix in melted white chocolate, then powdered sugar.",
            "Frost between layers and on top. Dust with extra matcha powder."
        ]
    },
    {
        "name": "German Black Forest Cake",
        "image": "/static/images/german-blackforest.jpg",
        "description": "A show-stopping chocolate sponge cake layered with cherry filling and whipped cream, decorated with chocolate shavings.",
        "category": "European",
        "difficulty": "Hard",
        "prep_time": "40 min",
        "bake_time": "30 min",
        "servings": 12,
        "ingredients": [
            "2 cups all-purpose flour",
            "2 cups sugar",
            "3/4 cup cocoa powder",
            "2 teaspoons baking soda",
            "1 teaspoon salt",
            "2 eggs",
            "1 cup buttermilk",
            "1 cup hot coffee",
            "1/2 cup vegetable oil",
            "1 can (21 oz) cherry pie filling",
            "3 cups heavy whipping cream",
            "1/3 cup powdered sugar",
            "Chocolate shavings for garnish",
            "Maraschino cherries for garnish"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease three 9-inch round pans.",
            "Whisk flour, sugar, cocoa, baking soda, and salt together.",
            "Add eggs, buttermilk, oil, and mix well. Stir in hot coffee.",
            "Divide batter among three pans and bake for 25-30 minutes.",
            "Cool completely on wire racks.",
            "Whip heavy cream with powdered sugar to stiff peaks.",
            "Place first layer on plate, top with cherry filling and whipped cream.",
            "Repeat with second layer.",
            "Place third layer on top, frost entirely with remaining whipped cream.",
            "Decorate with chocolate shavings and maraschino cherries.",
            "Refrigerate for at least 1 hour before serving."
        ]
    },
    {
        "name": "Tres Leches Cake",
        "image": "/static/images/tres-leches.jpg",
        "description": "A melt-in-your-mouth Latin American sponge cake soaked in three types of milk and topped with pillowy whipped cream.",
        "category": "Latin American",
        "difficulty": "Medium",
        "prep_time": "20 min",
        "bake_time": "25 min",
        "servings": 12,
        "ingredients": [
            "1 cup all-purpose flour",
            "1 1/2 teaspoons baking powder",
            "5 eggs",
            "1 cup sugar",
            "1/3 cup whole milk",
            "1 teaspoon vanilla extract",
            "1 can (14 oz) sweetened condensed milk",
            "1 can (12 oz) evaporated milk",
            "1 cup heavy cream",
            "2 cups heavy whipping cream (for topping)",
            "3 tablespoons sugar (for topping)",
            "Ground cinnamon for dusting"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease a 9x13 baking dish.",
            "Whisk flour and baking powder together.",
            "Beat eggs and sugar until pale, thick, and doubled in volume (about 5 minutes).",
            "Fold in flour mixture and milk alternately. Add vanilla.",
            "Pour into prepared dish and bake for 22-25 minutes.",
            "Mix condensed milk, evaporated milk, and 1 cup heavy cream together.",
            "When cake is done, poke holes all over with a fork.",
            "Pour the three-milk mixture slowly over the warm cake.",
            "Refrigerate for at least 4 hours or overnight to absorb the milk.",
            "Whip 2 cups cream with sugar, spread over cake, and dust with cinnamon."
        ]
    },
    {
        "name": "Blueberry Crumble Cake",
        "image": "/static/images/blueberry-crumble.jpg",
        "description": "A tender vanilla cake bursting with fresh blueberries, topped with a buttery, crunchy streusel crumble.",
        "category": "Fruit",
        "difficulty": "Easy",
        "prep_time": "20 min",
        "bake_time": "45 min",
        "servings": 10,
        "ingredients": [
            "2 cups all-purpose flour",
            "3/4 cup sugar",
            "2 teaspoons baking powder",
            "1/2 teaspoon salt",
            "1/2 cup butter, melted",
            "2 eggs",
            "3/4 cup milk",
            "1 teaspoon vanilla extract",
            "2 cups fresh blueberries",
            "1/2 cup flour (for crumble)",
            "1/3 cup sugar (for crumble)",
            "1/4 cup cold butter, cubed (for crumble)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease a 9-inch square or round pan.",
            "Whisk flour, sugar, baking powder, and salt together.",
            "In another bowl, mix melted butter, eggs, milk, and vanilla.",
            "Combine wet and dry ingredients until just mixed.",
            "Toss blueberries with 1 tablespoon flour, then gently fold into batter.",
            "Pour batter into prepared pan.",
            "For crumble: mix flour and sugar, cut in cold butter until pea-sized crumbs form.",
            "Scatter crumble topping over the batter.",
            "Bake for 40-45 minutes until golden and a toothpick comes out clean.",
            "Let cool 15 minutes before serving. Great warm or at room temperature."
        ]
    },
    {
        "name": "Coconut Layer Cake",
        "image": "/static/images/coconut.jpg",
        "description": "A tall, tropical coconut cake with coconut milk in the batter and a fluffy coconut cream cheese frosting coated in toasted coconut.",
        "category": "Tropical",
        "difficulty": "Medium",
        "prep_time": "25 min",
        "bake_time": "30 min",
        "servings": 14,
        "ingredients": [
            "2 1/2 cups all-purpose flour",
            "2 teaspoons baking powder",
            "1/2 teaspoon salt",
            "1 cup butter, softened",
            "1 3/4 cups sugar",
            "5 egg whites",
            "1 cup coconut milk",
            "1 teaspoon vanilla extract",
            "1 teaspoon coconut extract",
            "8 oz cream cheese (for frosting)",
            "1/2 cup butter (for frosting)",
            "4 cups powdered sugar (for frosting)",
            "2 cups sweetened shredded coconut, toasted"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease three 8-inch round pans.",
            "Whisk flour, baking powder, and salt together.",
            "Cream butter and sugar until light and fluffy.",
            "Add egg whites one at a time, beating well after each.",
            "Alternate adding flour mixture and coconut milk, starting and ending with flour.",
            "Stir in vanilla and coconut extract.",
            "Divide batter among three pans. Bake 25-30 minutes.",
            "Cool completely.",
            "For frosting: beat cream cheese and butter, gradually add powdered sugar.",
            "Frost between layers and cover the entire cake.",
            "Press toasted coconut onto the sides and top."
        ]
    },
    {
        "name": "Apple Cinnamon Cake",
        "image": "/static/images/apple-cinna.jpg",
        "description": "A warm, cozy cake loaded with tender apple chunks and swirled with cinnamon sugar. Tastes like autumn in every bite.",
        "category": "Fruit",
        "difficulty": "Easy",
        "prep_time": "20 min",
        "bake_time": "50 min",
        "servings": 12,
        "ingredients": [
            "3 cups all-purpose flour",
            "1 tablespoon baking powder",
            "1/2 teaspoon salt",
            "2 teaspoons cinnamon",
            "2 cups sugar",
            "1 cup vegetable oil",
            "4 eggs",
            "1/4 cup orange juice",
            "2 teaspoons vanilla extract",
            "3 medium apples, peeled and diced",
            "1/4 cup sugar mixed with 2 teaspoons cinnamon (for swirl)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease a 10-inch tube or bundt pan.",
            "Whisk flour, baking powder, salt, and cinnamon together.",
            "In a separate bowl, beat sugar, oil, eggs, orange juice, and vanilla.",
            "Gradually mix dry ingredients into wet ingredients.",
            "Toss diced apples into the batter.",
            "Pour 1/3 of batter into pan, sprinkle with cinnamon-sugar mixture.",
            "Repeat layers, ending with batter on top.",
            "Bake for 45-50 minutes until a toothpick comes out clean.",
            "Cool in pan for 15 minutes, then invert onto a plate.",
            "Dust with powdered sugar before serving."
        ]
    },
    {
        "name": "Pumpkin Spice Cake",
        "image": "/static/images/pumkin-spice.jpg",
        "description": "A deeply spiced, incredibly moist pumpkin cake with a swirl of cream cheese frosting. The ultimate fall dessert.",
        "category": "Seasonal",
        "difficulty": "Easy",
        "prep_time": "20 min",
        "bake_time": "35 min",
        "servings": 16,
        "ingredients": [
            "2 cups all-purpose flour",
            "2 teaspoons baking powder",
            "1 teaspoon baking soda",
            "2 teaspoons cinnamon",
            "1 teaspoon ginger",
            "1/2 teaspoon nutmeg",
            "1/4 teaspoon cloves",
            "1/2 teaspoon salt",
            "1 can (15 oz) pumpkin puree",
            "1 1/2 cups sugar",
            "4 eggs",
            "1 cup vegetable oil",
            "8 oz cream cheese (for frosting)",
            "1/4 cup butter (for frosting)",
            "2 cups powdered sugar (for frosting)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease a 9x13 pan or two 9-inch rounds.",
            "Whisk flour, baking powder, baking soda, and all spices together.",
            "In a large bowl, beat pumpkin, sugar, eggs, and oil until smooth.",
            "Add dry ingredients to wet and mix until just combined.",
            "Pour into prepared pan and bake for 30-35 minutes.",
            "Cool completely.",
            "For frosting: beat cream cheese and butter until smooth, then add powdered sugar.",
            "Spread frosting on cooled cake. Sprinkle with extra cinnamon if desired."
        ]
    },
    {
        "name": "Mango Mousse Cake",
        "image": "/static/images/mango-mousse.jpg",
        "description": "A tropical no-bake dessert with a buttery biscuit base and a silky, vibrant mango mousse layer. Refreshing and elegant.",
        "category": "Tropical",
        "difficulty": "Medium",
        "prep_time": "30 min",
        "bake_time": "No bake (chill 4+ hrs)",
        "servings": 8,
        "ingredients": [
            "2 cups crushed digestive biscuits (or graham crackers)",
            "1/2 cup melted butter",
            "2 large ripe mangoes (about 2 cups puree)",
            "1/2 cup sugar",
            "2 tablespoons gelatin powder",
            "1/4 cup warm water",
            "2 cups heavy whipping cream",
            "1 tablespoon lemon juice",
            "Extra mango slices for decoration"
        ],
        "steps": [
            "Mix crushed biscuits with melted butter. Press firmly into the bottom of an 8-inch springform pan.",
            "Refrigerate the base for 15 minutes.",
            "Blend mangoes until smooth. Stir in sugar and lemon juice.",
            "Sprinkle gelatin over warm water, let it bloom for 5 minutes, then microwave for 10 seconds.",
            "Stir dissolved gelatin into the mango puree.",
            "Whip heavy cream to soft peaks.",
            "Gently fold whipped cream into the mango mixture in two batches.",
            "Pour mousse over the chilled biscuit base.",
            "Refrigerate for at least 4 hours or until fully set.",
            "Decorate with fresh mango slices before serving."
        ]
    },
    {
        "name": "Chocolate Chip Cookie Cake",
        "image": "/static/images/choco-chip.jpg",
        "description": "A giant, soft-baked chocolate chip cookie in cake form. Crispy edges, chewy center, and perfect for cookie lovers.",
        "category": "Cookie",
        "difficulty": "Easy",
        "prep_time": "15 min",
        "bake_time": "25 min",
        "servings": 12,
        "ingredients": [
            "2 1/4 cups all-purpose flour",
            "1 teaspoon baking soda",
            "1 teaspoon salt",
            "1 cup butter, softened",
            "3/4 cup granulated sugar",
            "3/4 cup packed brown sugar",
            "2 eggs",
            "2 teaspoons vanilla extract",
            "2 cups semi-sweet chocolate chips",
            "Frosting of choice (optional)"
        ],
        "steps": [
            "Preheat oven to 350°F (175°C). Grease a 12-inch round pizza pan or cast iron skillet.",
            "Whisk flour, baking soda, and salt together.",
            "Cream butter, granulated sugar, and brown sugar until fluffy.",
            "Beat in eggs and vanilla.",
            "Gradually mix in flour mixture until just combined.",
            "Fold in chocolate chips.",
            "Press dough evenly into prepared pan.",
            "Bake for 22-25 minutes — the center should look slightly underdone (it will firm up).",
            "Cool for 10 minutes before slicing.",
            "Optionally pipe frosting around the edges and write a message!"
        ]
    }
]

# With --reset: clear all and insert seed data (removes any cakes you added).
# Without --reset: only insert seed data if the collection is empty (keeps your added cakes when you restart the app).
existing = collection.count_documents({})
if RESET:
    collection.delete_many({})
    print("Collection cleared.")
    result = collection.insert_many(cakes)
    print(f"Successfully inserted {len(result.inserted_ids)} seed cakes.")
elif existing == 0:
    result = collection.insert_many(cakes)
    print(f"Successfully inserted {len(result.inserted_ids)} seed cakes (collection was empty).")
else:
    print(f"Collection already has {existing} cake(s). Your added cakes are kept.")
    print("To clear everything and re-load only seed data, run:  python seed.py --reset")
    sys.exit(0)
print("\nCakes in seed:")
for cake in cakes:
    print(f"  - {cake['name']} ({cake['category']}, {cake['difficulty']})")
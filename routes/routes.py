from routes.__route import make_routes
from views.views import *


r = make_routes([
    ['/', home],
    ['/contacts', tracking]
])

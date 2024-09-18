from routes.__route import register_routes
from views.views import *


r = register_routes([
    ['/', home],
    ['/tracking', tracking]
])

from typing import override
from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Populates the database with sample data for Listing.'

    @override
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding Database'))
        self.stdout.write("Deleting existing Objects")
        Listing.objects.all().delete()

        listing_data = [
            {
                'name': 'Cozy Mountain Cabin',
                'description': 'A beautiful log cabin nestled in the mountains with stunning views and modern amenities.',
                'location': 'Aspen, Colorado',
                'price_per_night': 175.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440000'
            },
            {
                'name': 'Beachfront Villa with Private Pool',
                'description': 'Luxury villa steps away from the beach with a private pool and ocean view.',
                'location': 'Malibu, California',
                'price_per_night': 450.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440001'
            },
            {
                'name': 'Downtown Loft with City Views',
                'description': 'Modern loft in the heart of the city with amazing skyline views and walkable to all attractions.',
                'location': 'New York, New York',
                'price_per_night': 225.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440002'
            },
            {
                'name': 'Rustic Countryside Cottage',
                'description': 'Charming cottage surrounded by nature, perfect for a peaceful getaway.',
                'location': 'Vermont Countryside',
                'price_per_night': 120.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440003'
            },
            {
                'name': 'Luxury Penthouse Suite',
                'description': 'High-end penthouse with panoramic city views, modern design, and premium amenities.',
                'location': 'Miami, Florida',
                'price_per_night': 500.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440004'
            },
            {
                'name': 'Ski-in/Ski-out Chalet',
                'description': 'Direct access to the slopes from this cozy chalet with a fireplace and hot tub.',
                'location': 'Park City, Utah',
                'price_per_night': 350.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440005'
            },
            {
                'name': 'Historic Downtown Apartment',
                'description': 'Beautifully restored apartment in a historic building with modern comforts.',
                'location': 'Boston, Massachusetts',
                'price_per_night': 195.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440006'
            },
            {
                'name': 'Lakefront Cottage with Dock',
                'description': 'Peaceful cottage right on the lake with private dock and fishing gear included.',
                'location': 'Lake Tahoe, California',
                'price_per_night': 210.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440007'
            },
            {
                'name': 'Desert Oasis with Private Pool',
                'description': 'Stunning modern home in the desert with mountain views and private pool.',
                'location': 'Scottsdale, Arizona',
                'price_per_night': 275.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440008'
            },
            {
                'name': 'Vineyard Estate',
                'description': 'Elegant estate in the middle of a working vineyard with wine tasting included.',
                'location': 'Napa Valley, California',
                'price_per_night': 600.00,
                'host_id': '550e8400-e29b-41d4-a716-446655440009'
            }
        ]
        for item in listing_data:
            Listing.objects.create(**item)
        self.stdout.write(self.style.SUCCESS("Database Seeded"))
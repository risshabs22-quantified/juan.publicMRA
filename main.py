"""
Microsoft Rewards Automation Bot
================================

Automates Microsoft Rewards tasks including:
- Bing searches (PC and Mobile)
- Daily set activities
- More activities
- Punch cards
- Quizzes, polls, and more

Usage:
1. Copy config.example.json to config.json
2. Edit config.json with your Microsoft account credentials
3. Run: python main.py

WARNING: Use at your own risk. May violate Microsoft ToS.
"""

import json
import sys
from pathlib import Path

from src.browser import Browser
from src.auth import Auth
from src.searches import SearchAutomation
from src.rewards import RewardsAutomation
from src.utils import logger, print_banner, random_delay


def load_config() -> dict:
    """Load configuration from config.json."""
    config_path = Path(__file__).parent / "config.json"
    example_config_path = Path(__file__).parent / "config.example.json"
    
    if not config_path.exists():
        if example_config_path.exists():
            logger.error("config.json not found!")
            logger.error("Please copy config.example.json to config.json and add your credentials.")
        else:
            logger.error("config.json not found! Please create it with your credentials.")
        sys.exit(1)
        
    with open(config_path, "r") as f:
        config = json.load(f)
        
    # Validate required fields
    if config.get("email") == "YOUR_EMAIL@outlook.com":
        logger.error("Please update config.json with your actual email!")
        sys.exit(1)
        
    if config.get("password") == "YOUR_PASSWORD":
        logger.error("Please update config.json with your actual password!")
        sys.exit(1)
        
    return config


def run_bot():
    """Main bot execution."""
    print_banner()
    
    # Load configuration
    logger.info("Loading configuration...")
    config = load_config()
    
    email = config["email"]
    password = config["password"]
    headless = config.get("headless", False)
    pc_searches = config.get("pc_searches", 34)
    mobile_searches = config.get("mobile_searches", 24)
    min_delay = config.get("min_delay", 3)
    max_delay = config.get("max_delay", 8)
    
    logger.info(f"   Email: {email[:3]}***@{email.split('@')[1]}")
    logger.info(f"   Headless: {headless}")
    logger.info(f"   PC Searches: {pc_searches}")
    logger.info(f"   Mobile Searches: {mobile_searches}")
    
    total_points_before = 0
    total_points_after = 0
    
    # ===== DESKTOP BROWSER SESSION =====
    logger.info("\n" + "="*50)
    logger.info("STARTING DESKTOP SESSION")
    logger.info("="*50)
    
    try:
        with Browser(headless=headless, mobile=False) as browser:
            driver = browser.driver
            
            # Login
            auth = Auth(driver)
            if not auth.login(email, password):
                logger.error("Login failed! Please check your credentials.")
                return
            
            random_delay(2, 3)
            
            # Get initial points
            rewards = RewardsAutomation(driver)
            total_points_before = rewards.get_current_points()
            logger.info(f"Current points: {total_points_before:,}")
            
            # Perform PC searches
            search = SearchAutomation(driver, min_delay, max_delay)
            search.perform_searches(pc_searches, "PC")
            
            # Complete daily set
            rewards.complete_daily_set()
            
            # Complete more activities
            rewards.complete_more_activities()
            
            # Complete punch cards
            rewards.complete_punch_cards()
            
            # Get points after desktop session
            random_delay(2, 3)
            total_points_after = rewards.get_current_points()
            
    except Exception as e:
        logger.error(f"Desktop session error: {e}")
    
    # ===== MOBILE BROWSER SESSION =====
    logger.info("\n" + "="*50)
    logger.info("STARTING MOBILE SESSION")
    logger.info("="*50)
    
    try:
        with Browser(headless=headless, mobile=True) as browser:
            driver = browser.driver
            
            # Login again for mobile session
            auth = Auth(driver)
            if not auth.login(email, password):
                logger.error("Mobile login failed!")
            else:
                # Perform mobile searches
                search = SearchAutomation(driver, min_delay, max_delay)
                search.perform_searches(mobile_searches, "Mobile")
                
                # Get final points
                rewards = RewardsAutomation(driver)
                random_delay(2, 3)
                total_points_after = rewards.get_current_points()
                
    except Exception as e:
        logger.error(f"Mobile session error: {e}")
    
    # ===== SUMMARY =====
    logger.info("\n" + "="*50)
    logger.info("SESSION SUMMARY")
    logger.info("="*50)
    logger.info(f"   Points before: {total_points_before:,}")
    logger.info(f"   Points after:  {total_points_after:,}")
    logger.info(f"   Points earned: {total_points_after - total_points_before:,}")
    logger.info("="*50)
    logger.info("Bot completed! Thanks for using Microsoft Rewards Bot.")


if __name__ == "__main__":
    try:
        run_bot()
    except KeyboardInterrupt:
        logger.info("\nBot stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise

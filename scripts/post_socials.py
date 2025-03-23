import os
import abc
import requests
from typing import Dict, Any, Optional


class SocialMediaAdapter(abc.ABC):
    """Abstract base class for social media adapters following the adapter design pattern."""
    
    @abc.abstractmethod
    def post(self, content: str, media_url: Optional[str] = None) -> Dict[str, Any]:
        """
        Post content to a social media platform.
        
        Args:
            content: The text content to post
            media_url: Optional URL to media to include in the post
            
        Returns:
            Dict containing response information from the platform
        """
        pass


class XAdapter(SocialMediaAdapter):
    """Adapter for posting to X (formerly Twitter)."""
    
    def __init__(self):
        self.api_key = os.environ.get("X_API_KEY")
        self.api_secret = os.environ.get("X_API_SECRET")
        self.access_token = os.environ.get("X_ACCESS_TOKEN")
        self.access_secret = os.environ.get("X_ACCESS_SECRET")
        
        if not all([self.api_key, self.api_secret, self.access_token, self.access_secret]):
            raise ValueError("Missing required X API credentials in environment variables")
    
    def post(self, content: str, media_url: Optional[str] = None) -> Dict[str, Any]:
        # Implementation would use Twitter/X API
        # This is a placeholder for the actual implementation
        print(f"Posting to X: {content}")
        return {"platform": "X", "status": "success", "message": "Post created"}


class FacebookAdapter(SocialMediaAdapter):
    """Adapter for posting to Facebook."""
    
    def __init__(self):
        self.access_token = os.environ.get("FACEBOOK_ACCESS_TOKEN")
        self.page_id = os.environ.get("FACEBOOK_PAGE_ID")
        
        if not all([self.access_token, self.page_id]):
            raise ValueError("Missing required Facebook API credentials in environment variables")
    
    def post(self, content: str, media_url: Optional[str] = None) -> Dict[str, Any]:
        # Implementation would use Facebook Graph API
        # This is a placeholder for the actual implementation
        print(f"Posting to Facebook: {content}")
        return {"platform": "Facebook", "status": "success", "message": "Post created"}


class ThreadsAdapter(SocialMediaAdapter):
    """Adapter for posting to Threads."""
    
    def __init__(self):
        self.access_token = os.environ.get("THREADS_ACCESS_TOKEN")
        
        if not self.access_token:
            raise ValueError("Missing required Threads API credentials in environment variables")
    
    def post(self, content: str, media_url: Optional[str] = None) -> Dict[str, Any]:
        # Implementation would use Threads API
        # This is a placeholder for the actual implementation
        print(f"Posting to Threads: {content}")
        return {"platform": "Threads", "status": "success", "message": "Post created"}


class MastodonAdapter(SocialMediaAdapter):
    """Adapter for posting to Mastodon."""
    
    def __init__(self):
        self.access_token = os.environ.get("MASTODON_ACCESS_TOKEN")
        self.api_base_url = os.environ.get("MASTODON_INSTANCE_URL")
        
        if not all([self.access_token, self.api_base_url]):
            raise ValueError("Missing required Mastodon API credentials in environment variables")
    
    def post(self, content: str, media_url: Optional[str] = None) -> Dict[str, Any]:
        # Implementation would use Mastodon API
        # This is a placeholder for the actual implementation
        print(f"Posting to Mastodon: {content}")
        return {"platform": "Mastodon", "status": "success", "message": "Post created"}


class LinkedInAdapter(SocialMediaAdapter):
    """Adapter for posting to LinkedIn."""
    
    def __init__(self):
        self.access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
        self.organization_id = os.environ.get("LINKEDIN_ORGANIZATION_ID")
        
        if not all([self.access_token, self.organization_id]):
            raise ValueError("Missing required LinkedIn API credentials in environment variables")
    
    def post(self, content: str, media_url: Optional[str] = None) -> Dict[str, Any]:
        # Implementation would use LinkedIn API
        # This is a placeholder for the actual implementation
        print(f"Posting to LinkedIn: {content}")
        return {"platform": "LinkedIn", "status": "success", "message": "Post created"}


class SocialMediaManager:
    """
    Manager class that uses the adapter pattern to post to multiple social media platforms.
    """
    
    def __init__(self):
        self.adapters = []
    
    def add_adapter(self, adapter: SocialMediaAdapter):
        """Add a social media adapter to the manager."""
        self.adapters.append(adapter)
    
    def post_to_all(self, content: str, media_url: Optional[str] = None) -> Dict[str, Any]:
        """Post content to all configured social media platforms."""
        results = {}
        
        for adapter in self.adapters:
            try:
                platform_name = adapter.__class__.__name__
                results[platform_name] = adapter.post(content, media_url)
            except Exception as e:
                results[adapter.__class__.__name__] = {
                    "status": "error",
                    "message": str(e)
                }
        
        return results


# Example usage:
# manager = SocialMediaManager()
# manager.add_adapter(XAdapter())
# manager.add_adapter(FacebookAdapter())
# manager.add_adapter(ThreadsAdapter())
# manager.add_adapter(MastodonAdapter())
# manager.add_adapter(LinkedInAdapter())
# results = manager.post_to_all("Check out our new product!", "https://example.com/image.jpg")
